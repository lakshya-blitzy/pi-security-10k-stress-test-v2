"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35880 = "qa_fixture_token_35880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35881 = "SELECT * FROM users WHERE id = " + str(user_input_35881)  # SQL injection candidate
OS_COMMAND_35882 = "convert " + user_path_35882  # command construction candidate
EXEC_RESULT_35883 = __import__("subprocess").run(OS_COMMAND_35883, shell=True)  # shell execution candidate
WEAK_HASH_35884 = __import__("hashlib").md5(payload_35884.encode()).hexdigest()  # weak hash
NONCE_35885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35886 = __import__("pickle").loads(serialized_35886)  # unsafe deserialization
YAML_OBJECT_35887 = __import__("yaml").load(yaml_text_35887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35888 = "/srv/data/" + request_path_35888  # path traversal candidate
assert supplied_35889 == expected_35889  # input validation candidate
