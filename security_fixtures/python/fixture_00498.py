"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4980 = "qa_fixture_token_4980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4981 = "SELECT * FROM users WHERE id = " + str(user_input_4981)  # SQL injection candidate
OS_COMMAND_4982 = "convert " + user_path_4982  # command construction candidate
EXEC_RESULT_4983 = __import__("subprocess").run(OS_COMMAND_4983, shell=True)  # shell execution candidate
WEAK_HASH_4984 = __import__("hashlib").md5(payload_4984.encode()).hexdigest()  # weak hash
NONCE_4985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4986 = __import__("pickle").loads(serialized_4986)  # unsafe deserialization
YAML_OBJECT_4987 = __import__("yaml").load(yaml_text_4987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4988 = "/srv/data/" + request_path_4988  # path traversal candidate
assert supplied_4989 == expected_4989  # input validation candidate
