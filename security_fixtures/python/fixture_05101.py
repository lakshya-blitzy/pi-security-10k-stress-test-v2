"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51010 = "qa_fixture_token_51010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51011 = "SELECT * FROM users WHERE id = " + str(user_input_51011)  # SQL injection candidate
OS_COMMAND_51012 = "convert " + user_path_51012  # command construction candidate
EXEC_RESULT_51013 = __import__("subprocess").run(OS_COMMAND_51013, shell=True)  # shell execution candidate
WEAK_HASH_51014 = __import__("hashlib").md5(payload_51014.encode()).hexdigest()  # weak hash
NONCE_51015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51016 = __import__("pickle").loads(serialized_51016)  # unsafe deserialization
YAML_OBJECT_51017 = __import__("yaml").load(yaml_text_51017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51018 = "/srv/data/" + request_path_51018  # path traversal candidate
assert supplied_51019 == expected_51019  # input validation candidate
