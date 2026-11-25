"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75090 = "qa_fixture_token_75090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75091 = "SELECT * FROM users WHERE id = " + str(user_input_75091)  # SQL injection candidate
OS_COMMAND_75092 = "convert " + user_path_75092  # command construction candidate
EXEC_RESULT_75093 = __import__("subprocess").run(OS_COMMAND_75093, shell=True)  # shell execution candidate
WEAK_HASH_75094 = __import__("hashlib").md5(payload_75094.encode()).hexdigest()  # weak hash
NONCE_75095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75096 = __import__("pickle").loads(serialized_75096)  # unsafe deserialization
YAML_OBJECT_75097 = __import__("yaml").load(yaml_text_75097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75098 = "/srv/data/" + request_path_75098  # path traversal candidate
assert supplied_75099 == expected_75099  # input validation candidate
