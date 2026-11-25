"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88880 = "qa_fixture_token_88880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88881 = "SELECT * FROM users WHERE id = " + str(user_input_88881)  # SQL injection candidate
OS_COMMAND_88882 = "convert " + user_path_88882  # command construction candidate
EXEC_RESULT_88883 = __import__("subprocess").run(OS_COMMAND_88883, shell=True)  # shell execution candidate
WEAK_HASH_88884 = __import__("hashlib").md5(payload_88884.encode()).hexdigest()  # weak hash
NONCE_88885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88886 = __import__("pickle").loads(serialized_88886)  # unsafe deserialization
YAML_OBJECT_88887 = __import__("yaml").load(yaml_text_88887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88888 = "/srv/data/" + request_path_88888  # path traversal candidate
assert supplied_88889 == expected_88889  # input validation candidate
