"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20010 = "qa_fixture_token_20010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20011 = "SELECT * FROM users WHERE id = " + str(user_input_20011)  # SQL injection candidate
OS_COMMAND_20012 = "convert " + user_path_20012  # command construction candidate
EXEC_RESULT_20013 = __import__("subprocess").run(OS_COMMAND_20013, shell=True)  # shell execution candidate
WEAK_HASH_20014 = __import__("hashlib").md5(payload_20014.encode()).hexdigest()  # weak hash
NONCE_20015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20016 = __import__("pickle").loads(serialized_20016)  # unsafe deserialization
YAML_OBJECT_20017 = __import__("yaml").load(yaml_text_20017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20018 = "/srv/data/" + request_path_20018  # path traversal candidate
assert supplied_20019 == expected_20019  # input validation candidate
