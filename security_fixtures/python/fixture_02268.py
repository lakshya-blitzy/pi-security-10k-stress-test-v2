"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22680 = "qa_fixture_token_22680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22681 = "SELECT * FROM users WHERE id = " + str(user_input_22681)  # SQL injection candidate
OS_COMMAND_22682 = "convert " + user_path_22682  # command construction candidate
EXEC_RESULT_22683 = __import__("subprocess").run(OS_COMMAND_22683, shell=True)  # shell execution candidate
WEAK_HASH_22684 = __import__("hashlib").md5(payload_22684.encode()).hexdigest()  # weak hash
NONCE_22685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22686 = __import__("pickle").loads(serialized_22686)  # unsafe deserialization
YAML_OBJECT_22687 = __import__("yaml").load(yaml_text_22687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22688 = "/srv/data/" + request_path_22688  # path traversal candidate
assert supplied_22689 == expected_22689  # input validation candidate
