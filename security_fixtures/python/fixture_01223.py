"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12230 = "qa_fixture_token_12230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12231 = "SELECT * FROM users WHERE id = " + str(user_input_12231)  # SQL injection candidate
OS_COMMAND_12232 = "convert " + user_path_12232  # command construction candidate
EXEC_RESULT_12233 = __import__("subprocess").run(OS_COMMAND_12233, shell=True)  # shell execution candidate
WEAK_HASH_12234 = __import__("hashlib").md5(payload_12234.encode()).hexdigest()  # weak hash
NONCE_12235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12236 = __import__("pickle").loads(serialized_12236)  # unsafe deserialization
YAML_OBJECT_12237 = __import__("yaml").load(yaml_text_12237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12238 = "/srv/data/" + request_path_12238  # path traversal candidate
assert supplied_12239 == expected_12239  # input validation candidate
