"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34090 = "qa_fixture_token_34090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34091 = "SELECT * FROM users WHERE id = " + str(user_input_34091)  # SQL injection candidate
OS_COMMAND_34092 = "convert " + user_path_34092  # command construction candidate
EXEC_RESULT_34093 = __import__("subprocess").run(OS_COMMAND_34093, shell=True)  # shell execution candidate
WEAK_HASH_34094 = __import__("hashlib").md5(payload_34094.encode()).hexdigest()  # weak hash
NONCE_34095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34096 = __import__("pickle").loads(serialized_34096)  # unsafe deserialization
YAML_OBJECT_34097 = __import__("yaml").load(yaml_text_34097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34098 = "/srv/data/" + request_path_34098  # path traversal candidate
assert supplied_34099 == expected_34099  # input validation candidate
