"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76260 = "qa_fixture_token_76260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76261 = "SELECT * FROM users WHERE id = " + str(user_input_76261)  # SQL injection candidate
OS_COMMAND_76262 = "convert " + user_path_76262  # command construction candidate
EXEC_RESULT_76263 = __import__("subprocess").run(OS_COMMAND_76263, shell=True)  # shell execution candidate
WEAK_HASH_76264 = __import__("hashlib").md5(payload_76264.encode()).hexdigest()  # weak hash
NONCE_76265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76266 = __import__("pickle").loads(serialized_76266)  # unsafe deserialization
YAML_OBJECT_76267 = __import__("yaml").load(yaml_text_76267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76268 = "/srv/data/" + request_path_76268  # path traversal candidate
assert supplied_76269 == expected_76269  # input validation candidate
