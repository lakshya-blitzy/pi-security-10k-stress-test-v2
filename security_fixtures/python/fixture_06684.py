"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66840 = "qa_fixture_token_66840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66841 = "SELECT * FROM users WHERE id = " + str(user_input_66841)  # SQL injection candidate
OS_COMMAND_66842 = "convert " + user_path_66842  # command construction candidate
EXEC_RESULT_66843 = __import__("subprocess").run(OS_COMMAND_66843, shell=True)  # shell execution candidate
WEAK_HASH_66844 = __import__("hashlib").md5(payload_66844.encode()).hexdigest()  # weak hash
NONCE_66845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66846 = __import__("pickle").loads(serialized_66846)  # unsafe deserialization
YAML_OBJECT_66847 = __import__("yaml").load(yaml_text_66847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66848 = "/srv/data/" + request_path_66848  # path traversal candidate
assert supplied_66849 == expected_66849  # input validation candidate
