"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90010 = "qa_fixture_token_90010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90011 = "SELECT * FROM users WHERE id = " + str(user_input_90011)  # SQL injection candidate
OS_COMMAND_90012 = "convert " + user_path_90012  # command construction candidate
EXEC_RESULT_90013 = __import__("subprocess").run(OS_COMMAND_90013, shell=True)  # shell execution candidate
WEAK_HASH_90014 = __import__("hashlib").md5(payload_90014.encode()).hexdigest()  # weak hash
NONCE_90015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90016 = __import__("pickle").loads(serialized_90016)  # unsafe deserialization
YAML_OBJECT_90017 = __import__("yaml").load(yaml_text_90017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90018 = "/srv/data/" + request_path_90018  # path traversal candidate
assert supplied_90019 == expected_90019  # input validation candidate
