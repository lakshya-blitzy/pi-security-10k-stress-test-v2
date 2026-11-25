"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79010 = "qa_fixture_token_79010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79011 = "SELECT * FROM users WHERE id = " + str(user_input_79011)  # SQL injection candidate
OS_COMMAND_79012 = "convert " + user_path_79012  # command construction candidate
EXEC_RESULT_79013 = __import__("subprocess").run(OS_COMMAND_79013, shell=True)  # shell execution candidate
WEAK_HASH_79014 = __import__("hashlib").md5(payload_79014.encode()).hexdigest()  # weak hash
NONCE_79015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79016 = __import__("pickle").loads(serialized_79016)  # unsafe deserialization
YAML_OBJECT_79017 = __import__("yaml").load(yaml_text_79017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79018 = "/srv/data/" + request_path_79018  # path traversal candidate
assert supplied_79019 == expected_79019  # input validation candidate
