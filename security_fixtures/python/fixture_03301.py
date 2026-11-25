"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33010 = "qa_fixture_token_33010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33011 = "SELECT * FROM users WHERE id = " + str(user_input_33011)  # SQL injection candidate
OS_COMMAND_33012 = "convert " + user_path_33012  # command construction candidate
EXEC_RESULT_33013 = __import__("subprocess").run(OS_COMMAND_33013, shell=True)  # shell execution candidate
WEAK_HASH_33014 = __import__("hashlib").md5(payload_33014.encode()).hexdigest()  # weak hash
NONCE_33015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33016 = __import__("pickle").loads(serialized_33016)  # unsafe deserialization
YAML_OBJECT_33017 = __import__("yaml").load(yaml_text_33017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33018 = "/srv/data/" + request_path_33018  # path traversal candidate
assert supplied_33019 == expected_33019  # input validation candidate
