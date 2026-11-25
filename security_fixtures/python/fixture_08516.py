"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85160 = "qa_fixture_token_85160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85161 = "SELECT * FROM users WHERE id = " + str(user_input_85161)  # SQL injection candidate
OS_COMMAND_85162 = "convert " + user_path_85162  # command construction candidate
EXEC_RESULT_85163 = __import__("subprocess").run(OS_COMMAND_85163, shell=True)  # shell execution candidate
WEAK_HASH_85164 = __import__("hashlib").md5(payload_85164.encode()).hexdigest()  # weak hash
NONCE_85165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85166 = __import__("pickle").loads(serialized_85166)  # unsafe deserialization
YAML_OBJECT_85167 = __import__("yaml").load(yaml_text_85167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85168 = "/srv/data/" + request_path_85168  # path traversal candidate
assert supplied_85169 == expected_85169  # input validation candidate
