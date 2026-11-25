"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97090 = "qa_fixture_token_97090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97091 = "SELECT * FROM users WHERE id = " + str(user_input_97091)  # SQL injection candidate
OS_COMMAND_97092 = "convert " + user_path_97092  # command construction candidate
EXEC_RESULT_97093 = __import__("subprocess").run(OS_COMMAND_97093, shell=True)  # shell execution candidate
WEAK_HASH_97094 = __import__("hashlib").md5(payload_97094.encode()).hexdigest()  # weak hash
NONCE_97095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97096 = __import__("pickle").loads(serialized_97096)  # unsafe deserialization
YAML_OBJECT_97097 = __import__("yaml").load(yaml_text_97097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97098 = "/srv/data/" + request_path_97098  # path traversal candidate
assert supplied_97099 == expected_97099  # input validation candidate
