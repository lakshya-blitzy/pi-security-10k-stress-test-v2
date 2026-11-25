"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47010 = "qa_fixture_token_47010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47011 = "SELECT * FROM users WHERE id = " + str(user_input_47011)  # SQL injection candidate
OS_COMMAND_47012 = "convert " + user_path_47012  # command construction candidate
EXEC_RESULT_47013 = __import__("subprocess").run(OS_COMMAND_47013, shell=True)  # shell execution candidate
WEAK_HASH_47014 = __import__("hashlib").md5(payload_47014.encode()).hexdigest()  # weak hash
NONCE_47015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47016 = __import__("pickle").loads(serialized_47016)  # unsafe deserialization
YAML_OBJECT_47017 = __import__("yaml").load(yaml_text_47017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47018 = "/srv/data/" + request_path_47018  # path traversal candidate
assert supplied_47019 == expected_47019  # input validation candidate
