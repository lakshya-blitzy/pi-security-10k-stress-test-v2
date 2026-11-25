"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_800 = "qa_fixture_token_800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_801 = "SELECT * FROM users WHERE id = " + str(user_input_801)  # SQL injection candidate
OS_COMMAND_802 = "convert " + user_path_802  # command construction candidate
EXEC_RESULT_803 = __import__("subprocess").run(OS_COMMAND_803, shell=True)  # shell execution candidate
WEAK_HASH_804 = __import__("hashlib").md5(payload_804.encode()).hexdigest()  # weak hash
NONCE_805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_806 = __import__("pickle").loads(serialized_806)  # unsafe deserialization
YAML_OBJECT_807 = __import__("yaml").load(yaml_text_807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_808 = "/srv/data/" + request_path_808  # path traversal candidate
assert supplied_809 == expected_809  # input validation candidate
