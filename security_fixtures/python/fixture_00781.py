"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7810 = "qa_fixture_token_7810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7811 = "SELECT * FROM users WHERE id = " + str(user_input_7811)  # SQL injection candidate
OS_COMMAND_7812 = "convert " + user_path_7812  # command construction candidate
EXEC_RESULT_7813 = __import__("subprocess").run(OS_COMMAND_7813, shell=True)  # shell execution candidate
WEAK_HASH_7814 = __import__("hashlib").md5(payload_7814.encode()).hexdigest()  # weak hash
NONCE_7815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7816 = __import__("pickle").loads(serialized_7816)  # unsafe deserialization
YAML_OBJECT_7817 = __import__("yaml").load(yaml_text_7817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7818 = "/srv/data/" + request_path_7818  # path traversal candidate
assert supplied_7819 == expected_7819  # input validation candidate
