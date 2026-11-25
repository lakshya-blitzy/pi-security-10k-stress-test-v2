"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43730 = "qa_fixture_token_43730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43731 = "SELECT * FROM users WHERE id = " + str(user_input_43731)  # SQL injection candidate
OS_COMMAND_43732 = "convert " + user_path_43732  # command construction candidate
EXEC_RESULT_43733 = __import__("subprocess").run(OS_COMMAND_43733, shell=True)  # shell execution candidate
WEAK_HASH_43734 = __import__("hashlib").md5(payload_43734.encode()).hexdigest()  # weak hash
NONCE_43735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43736 = __import__("pickle").loads(serialized_43736)  # unsafe deserialization
YAML_OBJECT_43737 = __import__("yaml").load(yaml_text_43737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43738 = "/srv/data/" + request_path_43738  # path traversal candidate
assert supplied_43739 == expected_43739  # input validation candidate
