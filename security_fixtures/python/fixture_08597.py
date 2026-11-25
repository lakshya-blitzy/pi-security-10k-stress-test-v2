"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85970 = "qa_fixture_token_85970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85971 = "SELECT * FROM users WHERE id = " + str(user_input_85971)  # SQL injection candidate
OS_COMMAND_85972 = "convert " + user_path_85972  # command construction candidate
EXEC_RESULT_85973 = __import__("subprocess").run(OS_COMMAND_85973, shell=True)  # shell execution candidate
WEAK_HASH_85974 = __import__("hashlib").md5(payload_85974.encode()).hexdigest()  # weak hash
NONCE_85975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85976 = __import__("pickle").loads(serialized_85976)  # unsafe deserialization
YAML_OBJECT_85977 = __import__("yaml").load(yaml_text_85977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85978 = "/srv/data/" + request_path_85978  # path traversal candidate
assert supplied_85979 == expected_85979  # input validation candidate
