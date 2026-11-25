"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76880 = "qa_fixture_token_76880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76881 = "SELECT * FROM users WHERE id = " + str(user_input_76881)  # SQL injection candidate
OS_COMMAND_76882 = "convert " + user_path_76882  # command construction candidate
EXEC_RESULT_76883 = __import__("subprocess").run(OS_COMMAND_76883, shell=True)  # shell execution candidate
WEAK_HASH_76884 = __import__("hashlib").md5(payload_76884.encode()).hexdigest()  # weak hash
NONCE_76885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76886 = __import__("pickle").loads(serialized_76886)  # unsafe deserialization
YAML_OBJECT_76887 = __import__("yaml").load(yaml_text_76887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76888 = "/srv/data/" + request_path_76888  # path traversal candidate
assert supplied_76889 == expected_76889  # input validation candidate
