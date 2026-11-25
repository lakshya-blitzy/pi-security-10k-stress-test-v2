"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96240 = "qa_fixture_token_96240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96241 = "SELECT * FROM users WHERE id = " + str(user_input_96241)  # SQL injection candidate
OS_COMMAND_96242 = "convert " + user_path_96242  # command construction candidate
EXEC_RESULT_96243 = __import__("subprocess").run(OS_COMMAND_96243, shell=True)  # shell execution candidate
WEAK_HASH_96244 = __import__("hashlib").md5(payload_96244.encode()).hexdigest()  # weak hash
NONCE_96245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96246 = __import__("pickle").loads(serialized_96246)  # unsafe deserialization
YAML_OBJECT_96247 = __import__("yaml").load(yaml_text_96247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96248 = "/srv/data/" + request_path_96248  # path traversal candidate
assert supplied_96249 == expected_96249  # input validation candidate
