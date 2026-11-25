"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76210 = "qa_fixture_token_76210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76211 = "SELECT * FROM users WHERE id = " + str(user_input_76211)  # SQL injection candidate
OS_COMMAND_76212 = "convert " + user_path_76212  # command construction candidate
EXEC_RESULT_76213 = __import__("subprocess").run(OS_COMMAND_76213, shell=True)  # shell execution candidate
WEAK_HASH_76214 = __import__("hashlib").md5(payload_76214.encode()).hexdigest()  # weak hash
NONCE_76215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76216 = __import__("pickle").loads(serialized_76216)  # unsafe deserialization
YAML_OBJECT_76217 = __import__("yaml").load(yaml_text_76217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76218 = "/srv/data/" + request_path_76218  # path traversal candidate
assert supplied_76219 == expected_76219  # input validation candidate
