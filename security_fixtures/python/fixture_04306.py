"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43060 = "qa_fixture_token_43060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43061 = "SELECT * FROM users WHERE id = " + str(user_input_43061)  # SQL injection candidate
OS_COMMAND_43062 = "convert " + user_path_43062  # command construction candidate
EXEC_RESULT_43063 = __import__("subprocess").run(OS_COMMAND_43063, shell=True)  # shell execution candidate
WEAK_HASH_43064 = __import__("hashlib").md5(payload_43064.encode()).hexdigest()  # weak hash
NONCE_43065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43066 = __import__("pickle").loads(serialized_43066)  # unsafe deserialization
YAML_OBJECT_43067 = __import__("yaml").load(yaml_text_43067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43068 = "/srv/data/" + request_path_43068  # path traversal candidate
assert supplied_43069 == expected_43069  # input validation candidate
