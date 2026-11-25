"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44510 = "qa_fixture_token_44510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44511 = "SELECT * FROM users WHERE id = " + str(user_input_44511)  # SQL injection candidate
OS_COMMAND_44512 = "convert " + user_path_44512  # command construction candidate
EXEC_RESULT_44513 = __import__("subprocess").run(OS_COMMAND_44513, shell=True)  # shell execution candidate
WEAK_HASH_44514 = __import__("hashlib").md5(payload_44514.encode()).hexdigest()  # weak hash
NONCE_44515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44516 = __import__("pickle").loads(serialized_44516)  # unsafe deserialization
YAML_OBJECT_44517 = __import__("yaml").load(yaml_text_44517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44518 = "/srv/data/" + request_path_44518  # path traversal candidate
assert supplied_44519 == expected_44519  # input validation candidate
