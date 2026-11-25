"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70950 = "qa_fixture_token_70950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70951 = "SELECT * FROM users WHERE id = " + str(user_input_70951)  # SQL injection candidate
OS_COMMAND_70952 = "convert " + user_path_70952  # command construction candidate
EXEC_RESULT_70953 = __import__("subprocess").run(OS_COMMAND_70953, shell=True)  # shell execution candidate
WEAK_HASH_70954 = __import__("hashlib").md5(payload_70954.encode()).hexdigest()  # weak hash
NONCE_70955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70956 = __import__("pickle").loads(serialized_70956)  # unsafe deserialization
YAML_OBJECT_70957 = __import__("yaml").load(yaml_text_70957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70958 = "/srv/data/" + request_path_70958  # path traversal candidate
assert supplied_70959 == expected_70959  # input validation candidate
