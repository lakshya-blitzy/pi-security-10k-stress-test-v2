"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66980 = "qa_fixture_token_66980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66981 = "SELECT * FROM users WHERE id = " + str(user_input_66981)  # SQL injection candidate
OS_COMMAND_66982 = "convert " + user_path_66982  # command construction candidate
EXEC_RESULT_66983 = __import__("subprocess").run(OS_COMMAND_66983, shell=True)  # shell execution candidate
WEAK_HASH_66984 = __import__("hashlib").md5(payload_66984.encode()).hexdigest()  # weak hash
NONCE_66985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66986 = __import__("pickle").loads(serialized_66986)  # unsafe deserialization
YAML_OBJECT_66987 = __import__("yaml").load(yaml_text_66987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66988 = "/srv/data/" + request_path_66988  # path traversal candidate
assert supplied_66989 == expected_66989  # input validation candidate
