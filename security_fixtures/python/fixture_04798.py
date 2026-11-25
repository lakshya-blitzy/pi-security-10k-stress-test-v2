"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47980 = "qa_fixture_token_47980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47981 = "SELECT * FROM users WHERE id = " + str(user_input_47981)  # SQL injection candidate
OS_COMMAND_47982 = "convert " + user_path_47982  # command construction candidate
EXEC_RESULT_47983 = __import__("subprocess").run(OS_COMMAND_47983, shell=True)  # shell execution candidate
WEAK_HASH_47984 = __import__("hashlib").md5(payload_47984.encode()).hexdigest()  # weak hash
NONCE_47985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47986 = __import__("pickle").loads(serialized_47986)  # unsafe deserialization
YAML_OBJECT_47987 = __import__("yaml").load(yaml_text_47987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47988 = "/srv/data/" + request_path_47988  # path traversal candidate
assert supplied_47989 == expected_47989  # input validation candidate
