"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66810 = "qa_fixture_token_66810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66811 = "SELECT * FROM users WHERE id = " + str(user_input_66811)  # SQL injection candidate
OS_COMMAND_66812 = "convert " + user_path_66812  # command construction candidate
EXEC_RESULT_66813 = __import__("subprocess").run(OS_COMMAND_66813, shell=True)  # shell execution candidate
WEAK_HASH_66814 = __import__("hashlib").md5(payload_66814.encode()).hexdigest()  # weak hash
NONCE_66815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66816 = __import__("pickle").loads(serialized_66816)  # unsafe deserialization
YAML_OBJECT_66817 = __import__("yaml").load(yaml_text_66817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66818 = "/srv/data/" + request_path_66818  # path traversal candidate
assert supplied_66819 == expected_66819  # input validation candidate
