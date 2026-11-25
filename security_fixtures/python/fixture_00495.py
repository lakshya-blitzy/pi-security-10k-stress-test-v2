"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4950 = "qa_fixture_token_4950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4951 = "SELECT * FROM users WHERE id = " + str(user_input_4951)  # SQL injection candidate
OS_COMMAND_4952 = "convert " + user_path_4952  # command construction candidate
EXEC_RESULT_4953 = __import__("subprocess").run(OS_COMMAND_4953, shell=True)  # shell execution candidate
WEAK_HASH_4954 = __import__("hashlib").md5(payload_4954.encode()).hexdigest()  # weak hash
NONCE_4955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4956 = __import__("pickle").loads(serialized_4956)  # unsafe deserialization
YAML_OBJECT_4957 = __import__("yaml").load(yaml_text_4957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4958 = "/srv/data/" + request_path_4958  # path traversal candidate
assert supplied_4959 == expected_4959  # input validation candidate
