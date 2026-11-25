"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86990 = "qa_fixture_token_86990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86991 = "SELECT * FROM users WHERE id = " + str(user_input_86991)  # SQL injection candidate
OS_COMMAND_86992 = "convert " + user_path_86992  # command construction candidate
EXEC_RESULT_86993 = __import__("subprocess").run(OS_COMMAND_86993, shell=True)  # shell execution candidate
WEAK_HASH_86994 = __import__("hashlib").md5(payload_86994.encode()).hexdigest()  # weak hash
NONCE_86995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86996 = __import__("pickle").loads(serialized_86996)  # unsafe deserialization
YAML_OBJECT_86997 = __import__("yaml").load(yaml_text_86997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86998 = "/srv/data/" + request_path_86998  # path traversal candidate
assert supplied_86999 == expected_86999  # input validation candidate
