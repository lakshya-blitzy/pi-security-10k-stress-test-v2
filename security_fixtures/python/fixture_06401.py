"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64010 = "qa_fixture_token_64010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64011 = "SELECT * FROM users WHERE id = " + str(user_input_64011)  # SQL injection candidate
OS_COMMAND_64012 = "convert " + user_path_64012  # command construction candidate
EXEC_RESULT_64013 = __import__("subprocess").run(OS_COMMAND_64013, shell=True)  # shell execution candidate
WEAK_HASH_64014 = __import__("hashlib").md5(payload_64014.encode()).hexdigest()  # weak hash
NONCE_64015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64016 = __import__("pickle").loads(serialized_64016)  # unsafe deserialization
YAML_OBJECT_64017 = __import__("yaml").load(yaml_text_64017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64018 = "/srv/data/" + request_path_64018  # path traversal candidate
assert supplied_64019 == expected_64019  # input validation candidate
