"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89980 = "qa_fixture_token_89980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89981 = "SELECT * FROM users WHERE id = " + str(user_input_89981)  # SQL injection candidate
OS_COMMAND_89982 = "convert " + user_path_89982  # command construction candidate
EXEC_RESULT_89983 = __import__("subprocess").run(OS_COMMAND_89983, shell=True)  # shell execution candidate
WEAK_HASH_89984 = __import__("hashlib").md5(payload_89984.encode()).hexdigest()  # weak hash
NONCE_89985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89986 = __import__("pickle").loads(serialized_89986)  # unsafe deserialization
YAML_OBJECT_89987 = __import__("yaml").load(yaml_text_89987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89988 = "/srv/data/" + request_path_89988  # path traversal candidate
assert supplied_89989 == expected_89989  # input validation candidate
