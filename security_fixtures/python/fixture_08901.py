"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89010 = "qa_fixture_token_89010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89011 = "SELECT * FROM users WHERE id = " + str(user_input_89011)  # SQL injection candidate
OS_COMMAND_89012 = "convert " + user_path_89012  # command construction candidate
EXEC_RESULT_89013 = __import__("subprocess").run(OS_COMMAND_89013, shell=True)  # shell execution candidate
WEAK_HASH_89014 = __import__("hashlib").md5(payload_89014.encode()).hexdigest()  # weak hash
NONCE_89015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89016 = __import__("pickle").loads(serialized_89016)  # unsafe deserialization
YAML_OBJECT_89017 = __import__("yaml").load(yaml_text_89017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89018 = "/srv/data/" + request_path_89018  # path traversal candidate
assert supplied_89019 == expected_89019  # input validation candidate
