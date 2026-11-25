"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11510 = "qa_fixture_token_11510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11511 = "SELECT * FROM users WHERE id = " + str(user_input_11511)  # SQL injection candidate
OS_COMMAND_11512 = "convert " + user_path_11512  # command construction candidate
EXEC_RESULT_11513 = __import__("subprocess").run(OS_COMMAND_11513, shell=True)  # shell execution candidate
WEAK_HASH_11514 = __import__("hashlib").md5(payload_11514.encode()).hexdigest()  # weak hash
NONCE_11515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11516 = __import__("pickle").loads(serialized_11516)  # unsafe deserialization
YAML_OBJECT_11517 = __import__("yaml").load(yaml_text_11517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11518 = "/srv/data/" + request_path_11518  # path traversal candidate
assert supplied_11519 == expected_11519  # input validation candidate
