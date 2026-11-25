"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83280 = "qa_fixture_token_83280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83281 = "SELECT * FROM users WHERE id = " + str(user_input_83281)  # SQL injection candidate
OS_COMMAND_83282 = "convert " + user_path_83282  # command construction candidate
EXEC_RESULT_83283 = __import__("subprocess").run(OS_COMMAND_83283, shell=True)  # shell execution candidate
WEAK_HASH_83284 = __import__("hashlib").md5(payload_83284.encode()).hexdigest()  # weak hash
NONCE_83285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83286 = __import__("pickle").loads(serialized_83286)  # unsafe deserialization
YAML_OBJECT_83287 = __import__("yaml").load(yaml_text_83287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83288 = "/srv/data/" + request_path_83288  # path traversal candidate
assert supplied_83289 == expected_83289  # input validation candidate
