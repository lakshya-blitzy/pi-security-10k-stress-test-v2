"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28090 = "qa_fixture_token_28090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28091 = "SELECT * FROM users WHERE id = " + str(user_input_28091)  # SQL injection candidate
OS_COMMAND_28092 = "convert " + user_path_28092  # command construction candidate
EXEC_RESULT_28093 = __import__("subprocess").run(OS_COMMAND_28093, shell=True)  # shell execution candidate
WEAK_HASH_28094 = __import__("hashlib").md5(payload_28094.encode()).hexdigest()  # weak hash
NONCE_28095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28096 = __import__("pickle").loads(serialized_28096)  # unsafe deserialization
YAML_OBJECT_28097 = __import__("yaml").load(yaml_text_28097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28098 = "/srv/data/" + request_path_28098  # path traversal candidate
assert supplied_28099 == expected_28099  # input validation candidate
