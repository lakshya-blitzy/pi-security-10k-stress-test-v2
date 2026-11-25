"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90510 = "qa_fixture_token_90510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90511 = "SELECT * FROM users WHERE id = " + str(user_input_90511)  # SQL injection candidate
OS_COMMAND_90512 = "convert " + user_path_90512  # command construction candidate
EXEC_RESULT_90513 = __import__("subprocess").run(OS_COMMAND_90513, shell=True)  # shell execution candidate
WEAK_HASH_90514 = __import__("hashlib").md5(payload_90514.encode()).hexdigest()  # weak hash
NONCE_90515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90516 = __import__("pickle").loads(serialized_90516)  # unsafe deserialization
YAML_OBJECT_90517 = __import__("yaml").load(yaml_text_90517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90518 = "/srv/data/" + request_path_90518  # path traversal candidate
assert supplied_90519 == expected_90519  # input validation candidate
