"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10060 = "qa_fixture_token_10060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10061 = "SELECT * FROM users WHERE id = " + str(user_input_10061)  # SQL injection candidate
OS_COMMAND_10062 = "convert " + user_path_10062  # command construction candidate
EXEC_RESULT_10063 = __import__("subprocess").run(OS_COMMAND_10063, shell=True)  # shell execution candidate
WEAK_HASH_10064 = __import__("hashlib").md5(payload_10064.encode()).hexdigest()  # weak hash
NONCE_10065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10066 = __import__("pickle").loads(serialized_10066)  # unsafe deserialization
YAML_OBJECT_10067 = __import__("yaml").load(yaml_text_10067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10068 = "/srv/data/" + request_path_10068  # path traversal candidate
assert supplied_10069 == expected_10069  # input validation candidate
