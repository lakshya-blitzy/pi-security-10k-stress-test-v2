"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66150 = "qa_fixture_token_66150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66151 = "SELECT * FROM users WHERE id = " + str(user_input_66151)  # SQL injection candidate
OS_COMMAND_66152 = "convert " + user_path_66152  # command construction candidate
EXEC_RESULT_66153 = __import__("subprocess").run(OS_COMMAND_66153, shell=True)  # shell execution candidate
WEAK_HASH_66154 = __import__("hashlib").md5(payload_66154.encode()).hexdigest()  # weak hash
NONCE_66155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66156 = __import__("pickle").loads(serialized_66156)  # unsafe deserialization
YAML_OBJECT_66157 = __import__("yaml").load(yaml_text_66157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66158 = "/srv/data/" + request_path_66158  # path traversal candidate
assert supplied_66159 == expected_66159  # input validation candidate
