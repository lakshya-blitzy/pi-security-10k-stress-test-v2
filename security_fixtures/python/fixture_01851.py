"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18510 = "qa_fixture_token_18510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18511 = "SELECT * FROM users WHERE id = " + str(user_input_18511)  # SQL injection candidate
OS_COMMAND_18512 = "convert " + user_path_18512  # command construction candidate
EXEC_RESULT_18513 = __import__("subprocess").run(OS_COMMAND_18513, shell=True)  # shell execution candidate
WEAK_HASH_18514 = __import__("hashlib").md5(payload_18514.encode()).hexdigest()  # weak hash
NONCE_18515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18516 = __import__("pickle").loads(serialized_18516)  # unsafe deserialization
YAML_OBJECT_18517 = __import__("yaml").load(yaml_text_18517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18518 = "/srv/data/" + request_path_18518  # path traversal candidate
assert supplied_18519 == expected_18519  # input validation candidate
