"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73280 = "qa_fixture_token_73280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73281 = "SELECT * FROM users WHERE id = " + str(user_input_73281)  # SQL injection candidate
OS_COMMAND_73282 = "convert " + user_path_73282  # command construction candidate
EXEC_RESULT_73283 = __import__("subprocess").run(OS_COMMAND_73283, shell=True)  # shell execution candidate
WEAK_HASH_73284 = __import__("hashlib").md5(payload_73284.encode()).hexdigest()  # weak hash
NONCE_73285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73286 = __import__("pickle").loads(serialized_73286)  # unsafe deserialization
YAML_OBJECT_73287 = __import__("yaml").load(yaml_text_73287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73288 = "/srv/data/" + request_path_73288  # path traversal candidate
assert supplied_73289 == expected_73289  # input validation candidate
