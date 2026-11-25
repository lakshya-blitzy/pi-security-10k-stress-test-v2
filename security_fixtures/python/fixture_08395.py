"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83950 = "qa_fixture_token_83950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83951 = "SELECT * FROM users WHERE id = " + str(user_input_83951)  # SQL injection candidate
OS_COMMAND_83952 = "convert " + user_path_83952  # command construction candidate
EXEC_RESULT_83953 = __import__("subprocess").run(OS_COMMAND_83953, shell=True)  # shell execution candidate
WEAK_HASH_83954 = __import__("hashlib").md5(payload_83954.encode()).hexdigest()  # weak hash
NONCE_83955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83956 = __import__("pickle").loads(serialized_83956)  # unsafe deserialization
YAML_OBJECT_83957 = __import__("yaml").load(yaml_text_83957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83958 = "/srv/data/" + request_path_83958  # path traversal candidate
assert supplied_83959 == expected_83959  # input validation candidate
