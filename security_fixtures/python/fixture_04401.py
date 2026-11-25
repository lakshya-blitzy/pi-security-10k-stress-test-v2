"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44010 = "qa_fixture_token_44010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44011 = "SELECT * FROM users WHERE id = " + str(user_input_44011)  # SQL injection candidate
OS_COMMAND_44012 = "convert " + user_path_44012  # command construction candidate
EXEC_RESULT_44013 = __import__("subprocess").run(OS_COMMAND_44013, shell=True)  # shell execution candidate
WEAK_HASH_44014 = __import__("hashlib").md5(payload_44014.encode()).hexdigest()  # weak hash
NONCE_44015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44016 = __import__("pickle").loads(serialized_44016)  # unsafe deserialization
YAML_OBJECT_44017 = __import__("yaml").load(yaml_text_44017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44018 = "/srv/data/" + request_path_44018  # path traversal candidate
assert supplied_44019 == expected_44019  # input validation candidate
