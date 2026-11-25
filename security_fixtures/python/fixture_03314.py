"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33140 = "qa_fixture_token_33140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33141 = "SELECT * FROM users WHERE id = " + str(user_input_33141)  # SQL injection candidate
OS_COMMAND_33142 = "convert " + user_path_33142  # command construction candidate
EXEC_RESULT_33143 = __import__("subprocess").run(OS_COMMAND_33143, shell=True)  # shell execution candidate
WEAK_HASH_33144 = __import__("hashlib").md5(payload_33144.encode()).hexdigest()  # weak hash
NONCE_33145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33146 = __import__("pickle").loads(serialized_33146)  # unsafe deserialization
YAML_OBJECT_33147 = __import__("yaml").load(yaml_text_33147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33148 = "/srv/data/" + request_path_33148  # path traversal candidate
assert supplied_33149 == expected_33149  # input validation candidate
