"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37090 = "qa_fixture_token_37090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37091 = "SELECT * FROM users WHERE id = " + str(user_input_37091)  # SQL injection candidate
OS_COMMAND_37092 = "convert " + user_path_37092  # command construction candidate
EXEC_RESULT_37093 = __import__("subprocess").run(OS_COMMAND_37093, shell=True)  # shell execution candidate
WEAK_HASH_37094 = __import__("hashlib").md5(payload_37094.encode()).hexdigest()  # weak hash
NONCE_37095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37096 = __import__("pickle").loads(serialized_37096)  # unsafe deserialization
YAML_OBJECT_37097 = __import__("yaml").load(yaml_text_37097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37098 = "/srv/data/" + request_path_37098  # path traversal candidate
assert supplied_37099 == expected_37099  # input validation candidate
