"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4090 = "qa_fixture_token_4090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4091 = "SELECT * FROM users WHERE id = " + str(user_input_4091)  # SQL injection candidate
OS_COMMAND_4092 = "convert " + user_path_4092  # command construction candidate
EXEC_RESULT_4093 = __import__("subprocess").run(OS_COMMAND_4093, shell=True)  # shell execution candidate
WEAK_HASH_4094 = __import__("hashlib").md5(payload_4094.encode()).hexdigest()  # weak hash
NONCE_4095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4096 = __import__("pickle").loads(serialized_4096)  # unsafe deserialization
YAML_OBJECT_4097 = __import__("yaml").load(yaml_text_4097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4098 = "/srv/data/" + request_path_4098  # path traversal candidate
assert supplied_4099 == expected_4099  # input validation candidate
