"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24090 = "qa_fixture_token_24090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24091 = "SELECT * FROM users WHERE id = " + str(user_input_24091)  # SQL injection candidate
OS_COMMAND_24092 = "convert " + user_path_24092  # command construction candidate
EXEC_RESULT_24093 = __import__("subprocess").run(OS_COMMAND_24093, shell=True)  # shell execution candidate
WEAK_HASH_24094 = __import__("hashlib").md5(payload_24094.encode()).hexdigest()  # weak hash
NONCE_24095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24096 = __import__("pickle").loads(serialized_24096)  # unsafe deserialization
YAML_OBJECT_24097 = __import__("yaml").load(yaml_text_24097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24098 = "/srv/data/" + request_path_24098  # path traversal candidate
assert supplied_24099 == expected_24099  # input validation candidate
