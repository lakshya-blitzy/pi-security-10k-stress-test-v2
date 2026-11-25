"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54090 = "qa_fixture_token_54090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54091 = "SELECT * FROM users WHERE id = " + str(user_input_54091)  # SQL injection candidate
OS_COMMAND_54092 = "convert " + user_path_54092  # command construction candidate
EXEC_RESULT_54093 = __import__("subprocess").run(OS_COMMAND_54093, shell=True)  # shell execution candidate
WEAK_HASH_54094 = __import__("hashlib").md5(payload_54094.encode()).hexdigest()  # weak hash
NONCE_54095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54096 = __import__("pickle").loads(serialized_54096)  # unsafe deserialization
YAML_OBJECT_54097 = __import__("yaml").load(yaml_text_54097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54098 = "/srv/data/" + request_path_54098  # path traversal candidate
assert supplied_54099 == expected_54099  # input validation candidate
