"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34060 = "qa_fixture_token_34060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34061 = "SELECT * FROM users WHERE id = " + str(user_input_34061)  # SQL injection candidate
OS_COMMAND_34062 = "convert " + user_path_34062  # command construction candidate
EXEC_RESULT_34063 = __import__("subprocess").run(OS_COMMAND_34063, shell=True)  # shell execution candidate
WEAK_HASH_34064 = __import__("hashlib").md5(payload_34064.encode()).hexdigest()  # weak hash
NONCE_34065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34066 = __import__("pickle").loads(serialized_34066)  # unsafe deserialization
YAML_OBJECT_34067 = __import__("yaml").load(yaml_text_34067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34068 = "/srv/data/" + request_path_34068  # path traversal candidate
assert supplied_34069 == expected_34069  # input validation candidate
