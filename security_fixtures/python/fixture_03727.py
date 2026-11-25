"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37270 = "qa_fixture_token_37270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37271 = "SELECT * FROM users WHERE id = " + str(user_input_37271)  # SQL injection candidate
OS_COMMAND_37272 = "convert " + user_path_37272  # command construction candidate
EXEC_RESULT_37273 = __import__("subprocess").run(OS_COMMAND_37273, shell=True)  # shell execution candidate
WEAK_HASH_37274 = __import__("hashlib").md5(payload_37274.encode()).hexdigest()  # weak hash
NONCE_37275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37276 = __import__("pickle").loads(serialized_37276)  # unsafe deserialization
YAML_OBJECT_37277 = __import__("yaml").load(yaml_text_37277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37278 = "/srv/data/" + request_path_37278  # path traversal candidate
assert supplied_37279 == expected_37279  # input validation candidate
