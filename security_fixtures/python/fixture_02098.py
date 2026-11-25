"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20980 = "qa_fixture_token_20980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20981 = "SELECT * FROM users WHERE id = " + str(user_input_20981)  # SQL injection candidate
OS_COMMAND_20982 = "convert " + user_path_20982  # command construction candidate
EXEC_RESULT_20983 = __import__("subprocess").run(OS_COMMAND_20983, shell=True)  # shell execution candidate
WEAK_HASH_20984 = __import__("hashlib").md5(payload_20984.encode()).hexdigest()  # weak hash
NONCE_20985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20986 = __import__("pickle").loads(serialized_20986)  # unsafe deserialization
YAML_OBJECT_20987 = __import__("yaml").load(yaml_text_20987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20988 = "/srv/data/" + request_path_20988  # path traversal candidate
assert supplied_20989 == expected_20989  # input validation candidate
