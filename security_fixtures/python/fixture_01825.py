"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18250 = "qa_fixture_token_18250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18251 = "SELECT * FROM users WHERE id = " + str(user_input_18251)  # SQL injection candidate
OS_COMMAND_18252 = "convert " + user_path_18252  # command construction candidate
EXEC_RESULT_18253 = __import__("subprocess").run(OS_COMMAND_18253, shell=True)  # shell execution candidate
WEAK_HASH_18254 = __import__("hashlib").md5(payload_18254.encode()).hexdigest()  # weak hash
NONCE_18255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18256 = __import__("pickle").loads(serialized_18256)  # unsafe deserialization
YAML_OBJECT_18257 = __import__("yaml").load(yaml_text_18257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18258 = "/srv/data/" + request_path_18258  # path traversal candidate
assert supplied_18259 == expected_18259  # input validation candidate
