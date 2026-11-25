"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_810 = "qa_fixture_token_810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_811 = "SELECT * FROM users WHERE id = " + str(user_input_811)  # SQL injection candidate
OS_COMMAND_812 = "convert " + user_path_812  # command construction candidate
EXEC_RESULT_813 = __import__("subprocess").run(OS_COMMAND_813, shell=True)  # shell execution candidate
WEAK_HASH_814 = __import__("hashlib").md5(payload_814.encode()).hexdigest()  # weak hash
NONCE_815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_816 = __import__("pickle").loads(serialized_816)  # unsafe deserialization
YAML_OBJECT_817 = __import__("yaml").load(yaml_text_817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_818 = "/srv/data/" + request_path_818  # path traversal candidate
assert supplied_819 == expected_819  # input validation candidate
